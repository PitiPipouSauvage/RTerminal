<?php

declare(strict_types=1);

/**
 * @project MNC Fernet
 * @link https://github.com/mnavarrocarter/fernet
 * @project mnavarrocarter/fernet
 * @author Matias Navarro-Carter mnavarrocarter@gmail.com
 * @license MIT
 * @copyright 2022 Matias Navarro-Carter
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace MNC\Rand;

/**
 * Random is an abstraction over a random bytes source.
 *
 * Type-hinting to this abstraction is useful for testing purposes.
 *
 * @see FixedRandom
 */
interface Random
{
    /**
     * Reads random bytes from a source.
     *
     * @param int $bytes The number of bytes to read
     *
     * @throws RandomError if there is a problem reading bytes from the source
     *
     * @return string The random bytes
     */
    public function read(int $bytes): string;
}
